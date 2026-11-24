#!/usr/bin/env bash
#
# Install / sync the ComfyFactorio "Mountain Fortress v3" scenario into a
# Factorio Profile Manager (FPM) profile so it can be played locally.
#
# The script copies this repository into <profile>/scenarios/Mountain_Fortress_v3/
# (excluding VCS / CI / docs / editor dotfiles) and makes sure the
# Mountain Fortress map is enabled in the installed control.lua.
#
# Re-running the script re-syncs the scenario with the repo (rsync --delete),
# so it is safe to run again after editing the scenario in this checkout.
#
# Override any path via environment variables:
#   SCENARIO_NAME   scenario folder name         (default: Mountain_Fortress_v3)
#   PROFILE_DIR     FPM profile directory         (default: .../profile/Mtn)
#   REPO_DIR        ComfyFactorio checkout         (default: dir of this script)

set -euo pipefail

SCENARIO_NAME="${SCENARIO_NAME:-Mountain_Fortress_v3}"
PROFILE_DIR="${PROFILE_DIR:-/mnt/c/Users/micro/AppData/Local/FPM/profile/Mtn}"
REPO_DIR="${REPO_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"

DEST_DIR="${PROFILE_DIR}/scenarios/${SCENARIO_NAME}"
CONTROL_FILE="${DEST_DIR}/control.lua"
REQUIRE_LINE="require 'maps.mountain_fortress_v3.main'"

echo "== ComfyFactorio scenario installer =="
echo "Source repo : ${REPO_DIR}"
echo "Destination : ${DEST_DIR}"
echo ""

# --- sanity checks ---
if [ ! -f "${REPO_DIR}/control.lua" ]; then
    echo "ERROR: ${REPO_DIR}/control.lua not found." >&2
    echo "       Set REPO_DIR to the ComfyFactorio checkout." >&2
    exit 1
fi

if [ ! -d "${PROFILE_DIR}/mods" ]; then
    echo "ERROR: profile not found: ${PROFILE_DIR}" >&2
    echo "       Expected a 'mods' subfolder. Set PROFILE_DIR." >&2
    exit 1
fi

# --- warn if the required addon mod is missing from the profile ---
if ! ls "${PROFILE_DIR}/mods/"MtnFortressAddons*.zip >/dev/null 2>&1; then
    echo "WARNING: MtnFortressAddons*.zip not found in ${PROFILE_DIR}/mods/" >&2
    echo "         The scenario errors on load without it." >&2
fi

# --- install / sync the scenario ---
mkdir -p "${DEST_DIR}"

rsync -a --delete --delete-excluded \
    --exclude '.git/' \
    --exclude '.github/' \
    --exclude 'docs/' \
    --exclude '.luacheckrc' \
    --exclude '.editorconfig' \
    --exclude '.gitignore' \
    --exclude 'scripts/' \
    --exclude '*.sh' \
    "${REPO_DIR}/" "${DEST_DIR}/"

# --- enable the Mountain Fortress map (idempotent) ---
if grep -q "^${REQUIRE_LINE}\$" "${CONTROL_FILE}"; then
    echo "OK: Mountain Fortress v3 already enabled in control.lua"
elif grep -q "^--${REQUIRE_LINE}\$" "${CONTROL_FILE}"; then
    sed -i "s|^--${REQUIRE_LINE}|${REQUIRE_LINE}|" "${CONTROL_FILE}"
    echo "OK: enabled '${REQUIRE_LINE}'"
else
    echo "WARNING: could not find the require line to enable in control.lua" >&2
fi

# --- verify ---
if grep -q "^${REQUIRE_LINE}\$" "${CONTROL_FILE}"; then
    echo "Verified: map require line present."
else
    echo "ERROR: failed to enable the map in ${CONTROL_FILE}" >&2
    exit 1
fi

echo ""
echo "Done. Scenario installed to:"
echo "  ${DEST_DIR}"
echo ""
echo "Next steps:"
echo "  1. Make sure MtnFortressAddons (and MtnFortressAddonsPt2 for Space Age)"
echo "     are enabled in the 'Mtn' profile's mod list."
echo "  2. Launch Factorio via FPM (Mtn profile) -> New game -> Scenarios ->"
echo "     ${SCENARIO_NAME}."

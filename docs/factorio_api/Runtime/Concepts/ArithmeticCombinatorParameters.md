---
title: ArithmeticCombinatorParameters
tags: [factorio-api, runtime, concept]
---
# ArithmeticCombinatorParameters

## Fields

### first_signal
- **Type:** [[SignalID]]
- **Optional**
First signal to use in an operation. If not specified, the second argument will be the value of `first_constant`.

### first_signal_networks
- **Type:** [[CircuitNetworkSelection]]
- **Optional**
Which circuit networks (red/green) to read `first_signal` from. Defaults to both.

### first_constant
- **Type:** [[int32]]
- **Optional**
Constant to use as the first argument of the operation. Has no effect when `first_signal` is set. Defaults to `0`.

### operation
- **Type:** [[ArithmeticCombinatorParameterOperation]]
- **Optional**
When not specified, defaults to `"*"`.

### second_signal
- **Type:** [[SignalID]]
- **Optional**
Second signal to use in an operation. If not specified, the second argument will be the value of `second_constant`.

### second_signal_networks
- **Type:** [[CircuitNetworkSelection]]
- **Optional**
Which circuit networks (red/green) to read `second_signal` from. Defaults to both.

### second_constant
- **Type:** [[int32]]
- **Optional**
Constant to use as the second argument of the operation. Has no effect when `second_signal` is set. Defaults to `0`.

### output_signal
- **Type:** [[SignalID]]
- **Optional**
Specifies the signal to output.

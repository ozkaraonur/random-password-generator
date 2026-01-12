# Random Password Generator 🛡️

A professional-grade, high-entropy password generator built with Python. Unlike standard random generators, this tool follows a **Security-by-Default** philosophy by enforcing industry-standard complexity and utilizing cryptographic randomness.

## Key Security Features
- **CSPRNG Implementation**: Uses the `secrets` module to ensure non-deterministic, cryptographically secure randomness.
- **Complexity Enforcement**: A validation loop guarantees that every generated password contains at least one uppercase letter, one lowercase letter, one digit, and one special character.
- **High-Entropy Standard**: Defaults to a 20-character length to provide maximum resistance against modern brute-force and dictionary attacks.

## Why this is Secure
Most basic generators use the `random` module, which is "pseudo-random" and can be predicted if the seed is discovered. **Sentinel Password Architect** uses system-level entropy to ensure the output is mathematically unpredictable.



## Technical Skills Applied
- **Cryptographic Scripting**: Implementing `secrets` for secure token generation.
- **Defensive Logic**: Utilizing `while` loops and membership testing to enforce strict security policies.
- **User Experience (UX) Security**: Designing a flow that prioritizes secure defaults over weak user-defined inputs.

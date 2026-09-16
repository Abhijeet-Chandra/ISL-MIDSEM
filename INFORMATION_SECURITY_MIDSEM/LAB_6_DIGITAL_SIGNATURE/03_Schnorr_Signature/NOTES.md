PROGRAM:
Schnorr signature

Purpose:
Demonstrate Schnorr signing and verification.

INPUT:
Message/data plus the documented key or parameters.

OUTPUT:
Ciphertext, digest, signature, decision, timings, or recovered data as applicable.

CORE IDEA:
Keep input handling separate from the core operation and output formatting.

FORMULA / ALGORITHM:
e=H(R||m); s=k+ex; verify g^s=R*y^e

IMPORTANT FUNCTIONS:
Core operation, inverse/verification operation, validation, and encoding helpers.

IMPORTANT VARIABLES:
message/data, key parameters, encoded bytes/integers, result.

WHAT I MUST UNDERSTAND:
Why the inverse or verification works; valid parameter sizes; what must be transmitted or retained.

COMMON MODIFICATIONS:
1. text input
2. tamper detection
3. validation and tamper/error cases

CAN COMBINE WITH:
1. hashing
2. socket/file transfer
3. signing or access control (only where the syllabus combination fits)

COMMON EXAM TRAPS:
1. Confusing text, bytes, hexadecimal, and integer representations.
2. Using invalid keys, nonces, IVs, or modular inverses.
3. Comparing formatted output instead of the exact original bytes.

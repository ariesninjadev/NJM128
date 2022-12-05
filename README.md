# njm128
NJM128 is the first hash that utilizes randomness to generate random figures (exponential randomness).

| Step | Occurrence |
|--|--|
| 1 | Basic Hash |
| 2 | Random on key |
| 3 | RAND Data table |
| 4 | RSA Inclusion |
| 5 | 3-6x Basic Hashes |
| 6 | Calculated Sums |
| 7 | Basic Hash |

In reality, there is no advantage of this system over SHA, with one exception. SHA handles keys individually, and in a practical sense only allows 1 key to be used per encryption. However, feeding njm128 an array of keys will utilize all of them (up to 64). This means that if these keys are stored in different locations, the system being protected is technically exponentially more secure. This can be achieved by having separate SQL tables, separate server subsections (Still insecure to DA), and separate servers altogether.

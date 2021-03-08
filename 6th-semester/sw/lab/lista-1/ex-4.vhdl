-- (modified) Acquired from: https://ghdl.readthedocs.io/en/latest/quick_start/README.html

ENTITY ex4 IS
    PORT (
        A : IN BIT;
        B : IN BIT;
        C : IN BIT;
        X : OUT BIT;
        Y : OUT BIT
    );
END ex4;

ARCHITECTURE rtl OF ex4 IS
BEGIN
    -- Compute.
    X <= (A OR B) NOR (B NOR C);
    Y <= (B NOR C) AND (A XOR C);
END rtl;

-- Acquired from: https://ghdl.readthedocs.io/en/latest/quick_start/README.html

ENTITY adder IS
    -- `i0`, `i1`, and the carry-in `ci` are inputs of the adder.
    -- `s` is the sum output, `co` is the carry-out.
    PORT (
        i0, i1 : IN BIT;
        ci : IN BIT;
        s : OUT BIT;
        co : OUT BIT
    );
END adder;

ARCHITECTURE rtl OF adder IS
BEGIN
    --  This full-adder architecture contains two concurrent assignments.
    --  Compute the sum.
    s <= i0 XOR i1 XOR ci;
    --  Compute the carry.
    co <= (i0 AND i1) OR (i0 AND ci) OR (i1 AND ci);
END rtl;

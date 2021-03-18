-- Acquired from: https://ghdl.readthedocs.io/en/latest/quick_start/README.html

--  A testbench has no ports.
ENTITY adder_tb IS
END adder_tb;

ARCHITECTURE behav OF adder_tb IS
    --  Declaration of the component that will be instantiated.
    COMPONENT adder
        PORT (
            i0, i1 : IN BIT;
            ci : IN BIT;
            s : OUT BIT;
            co : OUT BIT);
    END COMPONENT;

    --  Specifies which entity is bound with the component.
    FOR adder_0 : adder USE ENTITY work.adder;
    SIGNAL i0, i1, ci, s, co : BIT;
    BEGIN
    --  Component instantiation.
    adder_0 : adder PORT MAP(i0 => i0, i1 => i1, ci => ci, s => s, co => co);

    --  This process does the real job.
    PROCESS
        TYPE pattern_type IS RECORD
            --  The inputs of the adder.
            i0, i1, ci : BIT;
            --  The expected outputs of the adder.
            s, co : BIT;
        END RECORD;
        --  The patterns to apply.
        TYPE pattern_array IS ARRAY (NATURAL RANGE <>) OF pattern_type;
        CONSTANT patterns : pattern_array :=
        (('0', '0', '0', '0', '0'),
        ('0', '0', '1', '1', '0'),
        ('0', '1', '0', '1', '0'),
        ('0', '1', '1', '0', '1'),
        ('1', '0', '0', '1', '0'),
        ('1', '0', '1', '0', '1'),
        ('1', '1', '0', '0', '1'),
        ('1', '1', '1', '1', '1'));
    BEGIN
        --  Check each pattern.
        FOR i IN patterns'RANGE LOOP
            --  Set the inputs.
            i0 <= patterns(i).i0;
            i1 <= patterns(i).i1;
            ci <= patterns(i).ci;
            --  Wait for the results.
            WAIT FOR 1 ns;
            --  Check the outputs.
            ASSERT s = patterns(i).s
            REPORT "bad sum value" SEVERITY error;
            ASSERT co = patterns(i).co
            REPORT "bad carry out value" SEVERITY error;
        END LOOP;
        ASSERT false REPORT "end of test" SEVERITY note;
        --  Wait forever; this will finish the simulation.
        WAIT;
    END PROCESS;

END behav;

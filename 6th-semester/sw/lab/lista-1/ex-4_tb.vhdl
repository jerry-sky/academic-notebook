-- (modified) Acquired from: https://ghdl.readthedocs.io/en/latest/quick_start/README.html

--  A testbench has no ports.
ENTITY ex4_tb IS
END ex4_tb;

ARCHITECTURE behav OF ex4_tb IS
    --  Declaration of the component that will be instantiated.
    COMPONENT ex4
        PORT (
            A : IN BIT;
            B : IN BIT;
            C : IN BIT;
            X : OUT BIT;
            Y : OUT BIT
        );
    END COMPONENT;

    --  Specifies which entity is bound with the component.
    FOR ex4_0 : ex4 USE ENTITY work.ex4;
    SIGNAL A, B, C, X, Y : BIT;
BEGIN
    --  Component instantiation.
    ex4_0 : ex4 PORT MAP(A => A, B => B, C => C, X => X, Y => Y);

    --  This process does the real job.
    PROCESS
        TYPE pattern_type IS RECORD
            --  The inputs of ex4.
            A, B, C : BIT;
            --  The expected outputs of ex4.
            X, Y : BIT;
        END RECORD;
        --  The patterns to apply.
        TYPE pattern_array IS ARRAY (NATURAL RANGE <>) OF pattern_type;
        CONSTANT patterns : pattern_array :=
        (
        ('0', '0', '0', '0', '0'),
        ('1', '0', '0', '0', '1'),
        ('1', '1', '0', '0', '0'),
        ('1', '1', '1', '0', '0'),
        ('0', '1', '1', '0', '0'),
        ('0', '0', '1', '1', '0'),
        ('0', '1', '0', '0', '0'),
        ('1', '0', '1', '0', '0')
        );
    BEGIN
        --  Check each pattern.
        FOR i IN patterns'RANGE LOOP
            --  Set the inputs.
            A <= patterns(i).A;
            B <= patterns(i).B;
            C <= patterns(i).C;
            --  Wait for the results.
            WAIT FOR 1 ns;
            --  Check the outputs.
            ASSERT X = patterns(i).X
            REPORT "bad X value" SEVERITY error;
            ASSERT Y = patterns(i).Y
            REPORT "bad Y value" SEVERITY error;
        END LOOP;
        ASSERT false REPORT "end of test" SEVERITY note;
        --  Wait forever; this will finish the simulation.
        WAIT;
    END PROCESS;

END behav;

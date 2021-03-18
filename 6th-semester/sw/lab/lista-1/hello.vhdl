-- Acquired from: https://ghdl.readthedocs.io/en/latest/quick_start/README.html

--  Hello world program
USE std.textio.ALL; -- Imports the standard tetmptio package.

--  Defines a design entity, without any ports.
ENTITY hello_world IS
END hello_world;

ARCHITECTURE behaviour OF hello_world IS
BEGIN
    PROCESS
        VARIABLE l : line;
    BEGIN
        write (l, string'("Hello world!"));
        writeline (output, l);
        readline (input, l);
        writeline (output, l);
        WAIT;
    END PROCESS;
END behaviour;

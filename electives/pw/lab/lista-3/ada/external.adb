
package body External is

    procedure SleepForSomeTime (maxSleep: Natural) is
       gen: RAF.Generator;
       fraction: Float;
    begin
       RAF.Reset(gen);
       fraction := 1.0 / Float(maxSleep);
       delay Duration(fraction * RAF.Random(gen));
    end SleepForSomeTime;

end External;

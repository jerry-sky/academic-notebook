with Ada.Strings.Unbounded;
with Ada.Strings.Unbounded.Text_IO;
with Ada.Text_IO;
with Ada.Command_Line;
with Ada.Numerics.Float_Random;

package External is

    package STR renames Ada.Strings.Unbounded;
    package IO renames Ada.Strings.Unbounded.Text_IO;
    package IOB renames Ada.Text_IO;
    package CMD renames Ada.Command_Line;
    package RAF renames Ada.Numerics.Float_Random;

    function ToMString(Source: in String) return STR.Unbounded_String renames STR.To_Unbounded_String;

    procedure PrintUnbounded(S: in STR.Unbounded_String) renames IO.Put_Line;

    procedure PrintBounded(S: in String) renames IOB.Put_Line;

    subtype MString is STR.Unbounded_String;

    function ToString(Source: in MString) return String renames STR.To_String;

    function DeleteLeftCharacters(Source: in MString; From: in Positive; Through: in Natural) return MString renames STR.Delete;

    procedure SleepForSomeTime(maxSleep: Natural);

end External;

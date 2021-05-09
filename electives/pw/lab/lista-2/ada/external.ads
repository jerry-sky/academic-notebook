with Ada.Strings.Unbounded;
with Ada.Strings.Unbounded.Text_IO;
with Ada.Text_IO;
with Ada.Command_Line;

package External is

    package STR renames Ada.Strings.Unbounded;
    package IO renames Ada.Strings.Unbounded.Text_IO;
    package IOB renames Ada.Text_IO;
    package CMD renames Ada.Command_Line;

    function ToBString(Source: in String) return STR.Unbounded_String renames STR.To_Unbounded_String;

    procedure PrintUnbounded(S: in STR.Unbounded_String) renames IO.Put_Line;

    procedure PrintBounded(S: in String) renames IOB.Put_Line;

    subtype BString is STR.Unbounded_String;

end External;

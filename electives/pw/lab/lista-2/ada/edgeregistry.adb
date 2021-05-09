
package body EdgeRegistry is

    function Key(a: Natural; b: Natural) return BString is
    begin
        return ToBString(Natural'Image(a) & ";" & Natural'Image(b));
    end Key;

    procedure Register(map: in out HashMap; a: Natural; b: Natural) is
    begin
        map.Insert(Key(a, b), True);
    end Register;

    function Exists(map: HashMap; a: Natural; b: Natural) return Boolean is
    begin
        return map.Contains(Key(a, b));
    end Exists;

end EdgeRegistry;

Set objArgs = WScript.Arguments
strProcess = objArgs(0)
strComputer = "."
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colProcesses = objWMIService.ExecQuery("Select * from Win32_Process Where Name ='" & strProcess & "'")

If colProcesses.Count = 0 Then
    Wscript.Echo strProcess & " is not running."
Else
    Wscript.Echo strProcess & " is running."
    'Kill the process
    For Each objProcess in colProcesses
        objProcess.Terminate()
    Next

End If

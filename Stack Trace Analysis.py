# Stack Trace Analysis

# Write a function complex_operation that calls several nested functions and may raise an exception.
# If an exception occurs, catch it and extract the "raw" stack trace information using traceback.extract_tb().
# Print the information for each stack frame (file, line, function name, line text).
import traceback
def complex_operation():
    def inner_funcation1():
        def inner_funcation2():
            def inner_funcation3():
                raise ValueError ("An Error occurs")
            inner_funcation3()
        inner_funcation2()
    try:
        inner_funcation1()
    except ValueError as e:
        tp=traceback.extract_tb(e.__traceback__)
        for frame in tp:
            print(f"File {frame.filename},Line {frame.lineno},Funcation{frame.name},Code {frame.line}")
complex_operation()
        
        
        
      
        
        

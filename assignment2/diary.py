# ---- Task 1 ----

import traceback

try:
    with open("diary.txt", "a") as file:
        flag = True  # indicates first input       
        while True:
            if flag:
                new_line = input("What happened today? ")
                flag = False
            else:
                new_line = input("What else? ")
            
            file.write(new_line + "\n")
            if new_line == "done for now":
                break
   
# except Exception as e:
#    print(f"An error occurred reading the file: {e}")

except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")
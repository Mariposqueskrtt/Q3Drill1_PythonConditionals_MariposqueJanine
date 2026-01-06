from pyscript import display, document

def adding_numbers(e):
    num1 = float(document.getElementById("input1").value)
    num2 = float(document.getElementById("input2").value)
    #compute for average
    average = (num1 + num2) / 2
    
    if average >= 75:
        document.getElementById("output1").innerHTML = "Passed✅"
    else:
            document.getElementById("output1").innerHTML = "Failed❌"
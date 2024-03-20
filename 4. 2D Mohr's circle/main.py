# importing the neccessary modules
from pyscript import document
from pyscript import display
import matplotlib.pyplot as plt
import numpy as np


def calculate(*args, **kwargs):
    
    sigma_x = document.querySelector("#sigma_x").value
    sigma_y = document.querySelector("#sigma_y").value
    tau_xy = document.querySelector("#tau_xy").value
    w = document.querySelector("#w").value
    unit = document.querySelector("#unit").value

    if sigma_x == "" or sigma_y == "" or tau_xy == "" or w == "" or unit == "":
        print("Please enter some numbers.")
        return
    
    sigma_x = float(sigma_x)
    sigma_y = float(sigma_y)
    tau_xy = float(tau_xy)
    w = float(w)
    unit = str(unit)


    
        # w=eval(input('enter the transformation angle 𝞱 +ve for ccw and -ve for cw 𝞱='))
    𝞱=np.radians(w)    #to convert degree into radian  

    #divisions
    theta = np.linspace(0,2*np.pi,360)

    R=np.sqrt((0.5*(sigma_x-sigma_y))**2+tau_xy**2)

    S_avg = (sigma_x + sigma_y)/2


    #geting transformed stresses
    sigma_x1 = 0.5*(sigma_x+sigma_y)+0.5*(sigma_x-sigma_y)*np.cos(2*𝞱)+tau_xy*np.sin(2*𝞱)
    sigma_y1 = 0.5*(sigma_x+sigma_y)-0.5*(sigma_x-sigma_y)*np.cos(2*𝞱)-tau_xy*np.sin(2*𝞱)
    tau_xy1 = -0.5*(sigma_x-sigma_y)*np.sin(2*𝞱)+tau_xy*np.cos(2*𝞱)


    x = S_avg +R*np.cos(theta)
    y=R*np.sin(theta)

    #principal stress 
    sigma_1 = S_avg+R
    sigma_2 = S_avg-R

    #geting principal angle & shear stress angle
    𝞱p = np.degrees(0.5 * np.arctan(2 * tau_xy/(sigma_x - sigma_y)))
    𝞱s=𝞱p+45

    #show the graph
    plt.plot(x,y)
    plt.plot([S_avg-R-10,S_avg+R+10],[0,0],linestyle='--',color='black')
    plt.plot([S_avg,S_avg],[-R-10,R+10],linestyle='--',color='black')

    plt.plot([sigma_x,sigma_y],[-tau_xy,tau_xy],[sigma_x,sigma_x],[-tau_xy,0],[sigma_y,sigma_y],[tau_xy,0],linestyle='-',color='black')

    plt.title("Mohr circle")
    plt.xlabel(r'$\sigma$'" - Normal Stress")
    plt.ylabel(r'$\tau$'" - Shear Stress")

    plt.plot()
    display(plt, target="output")

    
    document.querySelector("#outputOne").innerText = f"{round(sigma_1,2)} {unit}"
    document.querySelector("#outputwo").innerText = f"{round(sigma_2,2)} {unit}"
    document.querySelector("#outputhree").innerText = f"{round(𝞱p,2)}° and {round(𝞱s,2)}°"
    document.querySelector("#outputFour").innerText = f"{round(sigma_x1,2)} {unit}"
    document.querySelector("#outputFive").innerText = f"{round(sigma_y1,2)} {unit}"
    document.querySelector("#outputSix").innerText = f"{round(tau_xy1,2)} {unit}"

    
def clear(*args, **kwargs):
    document.querySelector("#sigma_x").value = ""
    document.querySelector("#sigma_y").value = ""
    document.querySelector("#tau_xy").value = ""
    document.querySelector("#w").value = ""
    document.querySelector("#unit").value = ""
    document.querySelector("#output").innerText = ""
    document.querySelector("#outputOne").innerText = ""
    document.querySelector("#outputwo").innerText = ""
    document.querySelector("#outputhree").innerText = ""
    document.querySelector("#outputFour").innerText = ""
    document.querySelector("#outputFive").innerText = ""
    document.querySelector("#outputSix").innerText = ""
import streamlit as st  
from HardwareTools import *

# Streamlit app
st.title("Real-Time System Monitor")

MAX_COUNTER=10
cpuData=[]
memData=[]
gpuData=[]
stColumns=st.empty()
stPlot=st.empty()
while True:
    # Get system values
    memoryTotalGb,memoryAvailableGb,memoryUsedGb,memoryPercent = checkRAMValues()
    cpuPercent,cpuCount=checkCPUValues()        
    gpuPercent,gpuUsed,gpuTotal = checkGPUValues()
    # Save data
    cpuDats=saveData(cpuData,cpuPercent)
    gpuData=saveData(gpuData,gpuPercent)
    memData=saveData(memData,memoryPercent)
    # Aufruf der Funktion
    col1,col2,col3=stColumns.columns(3)
    with col1:
        with st.container(height=150,border=True):
            st.write(f"CPU usage: {cpuPercent}%")
            st.write(f"Used cores: {cpuCount}")
            st.write("        ")
    with col2:    
        with st.container(height=150,border=True):
            st.write(f"Memory usage: {memoryUsedGb:.2f} GB")    
            st.write(f"Memory usage: {memoryPercent:}%")
            st.write(f"Memory total: {memoryTotalGb:.2f} GB")
    with col3:    
        with st.container(height=150,border=True):
            if gpuPercent!=None:
                st.write(f"GPU available: {gpuUsed:.2f} GB")                
                st.write(f"GPU usage: {gpuPercent:.1f}%")
                st.write(f"GPU total: {gpuTotal:.2f} GB")                
            else:
                st.write(f"No GPU available!")                
    plotData(stPlot,cpuData,memData,gpuData)       

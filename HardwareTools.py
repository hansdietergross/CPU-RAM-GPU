import psutil
import GPUtil  
import matplotlib.pyplot as plt

def checkRAMValues():
    memoryInfo = psutil.virtual_memory()
    memoryTotalGb=memoryInfo.total/ (1024 ** 3) 
    memoryAvailableGb=memoryInfo.available/ (1024 ** 3)
    memoryUsedGb = memoryInfo.used / (1024 ** 3)  
    memoryPercent = memoryInfo.percent
    return  memoryTotalGb,memoryAvailableGb,memoryUsedGb,memoryPercent

def checkCPUValues():
    cpuPercent = psutil.cpu_percent(interval=1)
    cpuCount=psutil.cpu_count()    
    return cpuPercent,cpuCount

def checkGPUValues():
    try:
        gpuInfo = GPUtil.getGPUs()[0]
    except:
        return None,None,None
    gpuTotal=gpuInfo.memoryTotal/1024
    gpuUsed=gpuInfo.memoryUsed/1024
    gpuPercent=gpuInfo.memoryUtil*100
    return gpuPercent,gpuUsed,gpuTotal

def saveData(data,oneValue):
    MAX_VALUES=100
    if oneValue!=None:
        data+=[oneValue]
    return data[-MAX_VALUES:]

def plotData(stPlot,cpuData,memData,gpuData):
    plt.title('Real-Time System Monitor')
    plt.ylabel('%')
    plt.xlabel('Time')
    plt.grid(True)
    plt.ylim(0, 100)  # Setze die y-Achse von 0 bis 100
    plt.xticks([])
    plt.legend(loc='upper left')
    cpu_line, = plt.plot(cpuData, color='green', label='CPU')
    mem_line, = plt.plot(memData, color='blue', label='RAM')    
    if (gpuData!=[]):
        gpu_line, = plt.plot(gpuData, color='red')    
        plt.legend( loc='upper left')
    else:
        plt.legend([cpu_line, mem_line], ['CPU',  'Memory'], loc='upper left')
    stPlot.pyplot(plt)
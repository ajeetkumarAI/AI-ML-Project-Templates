## Import all the required libraries

def training():

    #1. Read the config file 
        #1.1 Refer to config_template file for creating config file
    
    #2. Set logging configuration
        #2.1 Log after each step
        #2.2 refer to logging_template file which contains a function "_set_logger" that can be leveraged to initialize the logs with a given filename
    
    #3. Load (Read) Raw Data
        #3.1 Read raw input filenames and file paths from config file.
    
    #4. Read processed data 
    
    #5. Model Building 
    
    #6. Compare the Models performance and find the best model
        #6.1 AutoML, Tpot can be used
    
    #7. Score on best model
        #7.1 Save the metrics in model registry
    
    #8. Save artifacts object
        #8.1 Artifacts like model and feature selection object can be saved in pickle file

    

if __name__ == "__main__":
    training()
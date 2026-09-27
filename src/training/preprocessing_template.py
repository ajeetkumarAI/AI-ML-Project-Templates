## Import all the required libraries

def preprocessing():
    
    #1. Read the config file 
        #1.1 Refer to config_template file for creating config file
    
    #2. Set logging configuration
        #2.1 Log after each step
        #2.2 refer to logging_template file which contains a function "_set_logger" that can be leveraged to initialize the logs with a given filename
    
    #3. Read raw input filenames and file paths from config file. Load (Read) Raw Data
    
    #4. Validate Data using data unit test (data,feature_dtype)
        #4.1 A few data unit tests are available in data_checks
    
    #5. Data Preprocessing
        #5.1 A few data preprocessing methods are handling missing values and categorical features
    
    #6. Validate Data using data unit test after preprocessing (data, feature_dtype)
    
    #7. Model Data Preparation
        #7.1 Feature Selection, Oversampling 
    
    #8. Validate Data using unit test after feature engineering 
    
    #9. Save intermediate file (Parquet format is recommended).
    

if __name__ == "__main__":
    preprocessing()
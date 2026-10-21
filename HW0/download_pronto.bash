mkdir pronto                # creates a folder named 'pronto'
cd pronto
echo "These are the pronto data from 2015" > README.txt

mkdir data                  # creates a folder named 'data'
cd data

# Downloads the Pronto bike data into the data directory as a .zip file
curl -O https://s3.amazonaws.com/pronto-data/open_data_year_one.zip >> Open_Data_Y1.zip
unzip	Open_Data_Y1.zip    # unzips the .zip file

head *.csv                  # show the first few lines of all the .csv files

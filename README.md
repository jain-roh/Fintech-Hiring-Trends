# A2_Fintech-Analysis
Google Codelab : https://codelabs-preview.appspot.com/?file_id=1587kQyFCBuz2GoGBCno3f3WbojxPtiVVphsBJvFQ_Dk#8

Docker Hub Link: https://hub.docker.com/r/rohitjain058/datascience

GitHub Link: https://github.com/phadkeraj/A2_Fintech-Analysis

DropBox Keywords: https://www.dropbox.com/home/DataScienceTeam9?preview=Keywords+and+Bucketing.xlsx
(Contains the Final List of Keywords)

DropBox Fintech_Data: https://www.dropbox.com/home/DataScienceTeam9?preview=Fintech_Data.csv
(Contains the Final Dataset Used for Analysis)

Luigi PipeLine Flow:
1. Generated a Merged Data Set containing Institution, URL, Position and Location which was hosted on Dropbox
2. Fetched this data from Dropbox and ran it against out Fintech/Non-Fintech Mechanism to generate new features
3. Uploaded the Final Dataset to Dropbox
4. Established a live connection from Dropbox for this data to Tableau Server, so as to generate visual outcomes

Steps to Reproduce the Luigi Pipeline:
1. Import the necessary Packages, i.e Luigi for pipelining, in our case
2. Download the code "pipeline_final.py" from the GitHub link mentioned above
3. The global namespaces for folders have been set automatically according to the OS, so there is no need to change file paths
4. Run "pipeline_final.py" 
5. This will generate the final output and post it on Dropbox so that Tableau Server can eastablish a live connection 

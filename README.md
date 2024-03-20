# pointsTableScraping
Installed selenium and Chrome Driver
at first I was having truble with Chrome driver with it's Path. After researching I placed the Chrome driver to main directory where i created my python file.
After that tried a simple code to redirect google.com which was successful 
Then inspected the WIKi Page and using Xpath trageted the teams entry point and tested that but got an error that **find_elements_by_xpath** has not attribute so I searched on Stackoverfolow and found that in selenium 4 the removed the **find_elements_by_xpath** and repleced with **find_elements("xpath",'')** then i got  the result
Then tragetd the Pts table and got the output and then imported json and stored the data in json format.

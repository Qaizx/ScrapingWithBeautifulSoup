from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=")
    soup = BeautifulSoup(html_text.text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    unfamiliar_skill = input("Enter a skill you are unfamiliar with: ")
    for index, job in enumerate(jobs): 
        # Extract publication date
        publication_date = job.find('span', class_='sim-posted').text.strip() 
        
        if 'few' in publication_date:
            # Extract job title
            job_title = job.find('h2').text.strip()
            # Extract company name
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            # Extract skills
            skills = job.find('div', class_='more-skills-sections').text.strip()
            # Clean up the skills text
            skills = ' '.join(skills.split())
            # More info link
            more_info = job.header.h2.a['href']
            
            if unfamiliar_skill.lower() not in skills.lower():
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Job Title: {job_title}\n")
                    f.write(f"Company Name: {company_name}\n")
                    f.write(f"Skills: {skills}\n")
                    f.write(f"Publication Date: {publication_date}\n")
                    f.write(f"More Info: {more_info}")
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        user_input = input("Do you want to search for jobs? (yes/no): ").strip().lower()
        if user_input == 'no':
            print("Exiting the job search.")
            break
        elif user_input == 'yes':
            find_jobs()
            time_wait = 10  # seconds
            print(f"Waiting for {time_wait} seconds before the next search...")
            time.sleep(time_wait)
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue
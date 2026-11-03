## Intro to cybersec 

- Introduce domains and carrer paths 
- Explain basically what is cyber sec . 
- Explain the most fundamental principal in cyber security .
## Intro to AI in cybersec .

- Explain the concept of logs and then just put this in chat gpt 

**PROMPT ( log analysis)
	`You are a cybersecurity analyst. Analyze these authentication logs for unusual activity. Identify the 3 most suspicious events, explain why each is suspicious in beginner-friendly language, and distinguish between an anomaly and confirmed malicious activity`
**PROMPT ( report writting)
`		Based on the authentication-log analysis you just performed, create a short, professional **Cybersecurity Log Analysis Report** suitable for presenting to a beginner-level cybersecurity team.`
	
	Include:
	
	1. **Executive Summary** — 2–3 sentences explaining the overall situation.
	    
	2. **Key Findings** — list the 3 most suspicious events identified from the logs.
	    
	3. **Why They Are Suspicious** — explain the indicators in simple language.
	    
	4. **Anomaly vs Confirmed Malicious Activity** — clearly distinguish what the logs prove from what they only suggest.
	    
	5. **Potential Impact** — briefly explain what could happen if the suspicious activity were actually malicious.
	    
	6. **Recommended Actions** — give practical defensive steps an analyst should take next.
	    
	7. **Final Assessment** — classify the overall situation as Low / Medium / High priority and explain why.
	    
	
	Use the actual evidence from the uploaded logs and do not invent events, users, IP addresses, timestamps, or conclusions that aren't supported by the data.
	
	Keep the report concise and readable. Use tables where they improve clarity.
	
	At the end, add a section titled **“AI Limitations”** explaining that this analysis identifies suspicious patterns but does not prove that an attack occurred; human investigation and additional security data would still be required.
	
	Format it like a real SOC analyst report that could be shared with a security team.
## ATO 

- When explaining brute forcing and credential sutffing , mention about how data breaches are very common and how you should also check if you **have  I been pwned** on have i been pwned website . 
- Do the **phishing attack sim from thm** room . 
- Real life news on how many attacks are done through phishing mails . 

## Now onto some real hacking 

- Tell the audience about **OWASP top 10** .  
- Tell the audience about injections .
- How frequently xss vuln occurs . 
- Do live demo on dvwa . 
  
  ### SQLi 

- Tell the concept .
- Show DVWA 
- Suggest parametrazisation / sanitation 
  
  ### XSS 
  
  - Tell the concept on how html /js renders comment box inputs.
  - Tell about input sanitazation , csp and 


## Security best practices 

- Password manager 
- MFA/2fA
- Carefully handling urls and pdfs that you encounter online . 
- Who is lookup 
- Temp-mail 
- Etc . 
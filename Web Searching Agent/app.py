from duckduckgo_search import DDGS
from swarm import Swarm, Agent
from datetime import datetime

current_time = datetime.now().strftime("%H:%M:%S")

# Create a new Swarm client
client = Swarm()

# Create internet search tool
def get_search_results(topic):
    print(f"Searching for {topic} at {current_time}")
    
    ddgs = DDGS()
    results = ddgs.text(f"{topic}", max_results=5)
    
    print(results)
    
    if results:
        #print(results)
        news_results = "\n".join([f"{i+1}. {result['title']} - {result['href']}" for i, result in enumerate(results)])
        print(news_results)
        return news_results
    else:
        return "No search results found."
    
    
# Create agents
def transfer_to_editor(raw_news):
    print(f"Transferring to editor at {current_time}")
    return editor_agent.run(messages=[{"role": "system", "content": raw_news}])

news_agent = Agent(
    name="News Agent",
    instructions="You are a news agent. Search for results for a given topic using DuckDuckGo search",             ###################################
    functions=[get_search_results],
    model="llama3.2",
)


editor_agent = Agent(
    name="Editor Agent",
    instructions="You are an editor agent",                 ##################################
    model="llama3.2",
)



# Create workflow
def run_news_workflow(topic):
    print(f"Running news workflow at {current_time}")
    
    news_results = client.run(
        agent=news_agent,
        messages=[{"role": "user", "content": "Australia"}],
    )
    
  #  print(news_results.messages)
    
    raw_news = news_results.messages[-1]["content"]
    
    print(f"Raw news: {raw_news}")
    
    edited_news = client.run(
        agent=editor_agent,
        messages=[{"role": "system", "content": raw_news}],
    )
    
   # print(edited_news.messages)
    
    return edited_news.messages[-1]["content"]

# Example usage
print(run_news_workflow("Hi"))
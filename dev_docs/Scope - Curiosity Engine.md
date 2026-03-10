An autonomous agent that explores the web based on curiosity.
It asks two questions:
- *What should I learn about?*
- *What strange things exists online?*

It will have two modes:
1. **Research Mode** -> Deep dive into a topic
2. **Discovery Mode** -> Wander the internet looking for strange or interesting things.

## Core Components

#### 1. Explorer Agent
Responsible for **visiting pages**.
Steps:
```
visit page
extract text
extract links
score curiosity
choose next page
```

#### 2. Curiosity Scoring System
**THE BRAIN**

Scores pages based on signals like:
**RESEARCH SIGNALS**
- topic relevance
- rare words
- technical vocabulary
- citations

**DISCOVERY SIGNALS**
- unusual domains
- deep URL paths
- strange HTML structures
- very old pages

Example scoring:
```
curiosity_score =
	rarirty_score
  + novelty_score
  + topic_relevance
  + weirdness_score
```

# Mode 1: Curiosity-Driven Research Agent

Input:
`topic = "ant colony behavior"`

Agent explores:
```
ant colony
-> pheromone signaling
-> swarm intelligence
-> distributed robotics
-> self organizing systems
```

It build a **knowledge graph**.

Example structure:
```
Ant colony  
	│  
	├─ pheromone communication  
	├─ division of labour  
	└─ swarm intelligence  
			│  
			└─ robotics
```

Output:
```
discovered topics
connections between ideas
summary of each page
```

# Mode 2: Autonomous Curiosity Engine

Instead of a topic, the agent asks:
> "What unusual things exist on the internet?"

Starting seeds:
```
random wikipedia
old blog directories
random domain generator
```

Signals for weirdness:
- domain older than **15 years**
- page has **< 10 links**
- strange keywords
- broken layouts
- long forgotten blogs

Example discovery:
```
Found:
 + 2003 blog about artificial life
 + abandoned swarm simulation project
 + weird forum discussing self evolving code
```

It builds a **daily curiosity report**

## Architecture

```
		Curiosity Engine  
			  │  
	┌─────────┴─────────┐  
	│                   │  
Research Agent    Discovery Agent  
	│                   │  
crawl topic crawl    random web  
	│                   │  
extract ideas     detect weird sites  
	│                   │  
knowledge graph   curiosity database
```

Tech Stack:
	Python works perfectly
	Core tools:
```
requests
beautifulsoup4
sqlite
networkx

playwright (screenshots)
sentence-transformers (topic similarity)
```

Example data structure:
```
Page
 ├ url
 ├ title
 ├ topic_score
 ├ weird_score
 ├ discovered_links
 └ timestamp
```
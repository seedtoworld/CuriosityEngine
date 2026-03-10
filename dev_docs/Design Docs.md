The Engine should answer two questions:

**RESEARCH MODE**
> Given a topic, explore the web and build a knowledge structure.

**DISCOVERY MODE**
> Autonomously explore the web to discover interesting or unusual content.

Outputs:
- knowledge graphs
- exploration paths
- interesting discoveries
- page summaries
- topic clusters

# Core System Architecture
```
                Curiosity Engine
                       │
        ┌──────────────┼──────────────┐
        │              │              │
   Crawl System   Curiosity Engine   Knowledge System
        │              │              │
   Page Fetcher    Page Scorer     Knowledge Graph
   Link Extractor  Novelty Model   Topic Clusters
   URL Queue       Strategy Agent  Summaries
```

Each part can evolve independently.

# Main System Components
### Frontier Manager (URL Queue)
The **HEART OF EXPLORATION**.

Stores URLs waiting to be explored.
Data stored:
```
url
depth
discovery_source
priority_score
visited
```

Selection strategy:
```
choose highest curiosity score
avoid duplicates
respect domain limits
```
This prevents crawler chaos.

### Page Fetcher

Responsible for **downloading pages safely**.

Requirements:
- respect robots.txt
- rate limit domains
- retry failures
- detect content type

Output:
```
html
metadata
response info
```

### Content Parser

Extract useful information.

```
title
text
links
keywords
structure
```

Also Compute:
```
word frequencies
topic signals
language
```

### Curiosity Engine (The Brain)

This decides **where to explore next**.

Curiosity score combines:
```
Novelty
Information density
Topic relevance
Weirdness
Exploration depth
```

Example formula:
```
curiosity_score = 
	novelty_score
  + rarity_score
  + topic_score
  + exploration_bonus
```

Signals:
- *Novelty*: Have we seen similar content before?
- *Rarity*: Rare terms -> higher curiosity
- *Weirdness*: Unusual HTML structures or words
- *Depth*: Deep pages often contain hidden info

### Knowledge System

Stores structured discoveries.

Use:
```
Knowledge Graph
Topic Index
Document Store
```

Example graph:
```
Swarm Intelligence
      │
      ├── Ant Colonies
      │       │
      │       └── Pheromone Communication
      │
      └── Distributed Robotics
```

### Discovery Database

Store interesting finds.

Example:
```
url
title
discovery_score
topic_cluster
first_seen
domain_age
```

### Data Storage

Start simple but scalable.
Tables:
```
pages
links
topics
discoveries
frontier
```

Graphs:
```
knowledge_graph
topic_relationships
```

### Exploration Strategies

Your agent can have **multiple strategies**.

Example:
- *Greed curiosity* -> Pick highest score.
- *Random exploration* -> Prevent local traps.
- *Topic deep dive* -> Stay within topic cluster.
- *Domain hopping* -> Discover new regions.

### Visualization Layer

Exploration becomes fun when visualized.

Exploration Graphs:
```
domain clusters
topic clusters
exploration paths
```

Discovery Feed:
```
Top discoveries today
Weirdest sites found
Deepest page reached
```

# Safety & Ethics

The crawler must:
- obey robots.txt
- limit request rate
- avoid login pages
- avoid infinite traps
- identify itself with a user agent

Example:
`CuriosityBot/0.1 (research crawler)`
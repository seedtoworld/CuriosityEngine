- [ ] Project skeleton created
- [ ] Minimal Crawler
- [ ] Frontier System
- [ ] Database
- [ ] Robust Crawling
- [ ] Curiosity scoring
- [ ] Research mode
- [ ] Discovery mode
- [ ] Multi-agent exploration
- [ ] Visualization
# Phase 0 - Project Foundation

Goals: Create a clean and maintainable project base.
- [x] Create repository for **CuriosityEngine**
- [x] Initialize project folder structure
- [x] Create project *README* explaining the vision
- [x] Define system architecture document
- [x] Define core data models
- [x] Create configuration system
- [x] Define crawler user-agent
- [x] Setup logging system

Deliverable:
- Clean project skeleton ready for development
# Phase 1 - Minimal Crawler

Goals: Confirm the system can crawl and extract links.
- [ ] Implement simple HTTP page fetcher
- [ ] Extract HTML content
- [ ] Parse page title
- [ ] Extract hyperlinks
- [ ] Normalize URLs
- [ ] Print discovered links
- [ ] Crawl starting from one seed URL

Deliverable:
- Crawler can visit pages and discover new URLs
# Phase 2 - Frontier System (URL Management)

Goals: Control **what the crawler visits next**.
- [ ] Implement URL frontier queue
- [ ] Add URL deduplication
- [ ] Track visited URLs
- [ ] Store URL depth
- [ ] Add priority scoring placeholder
- [ ] Limit frontier size

Deliverable:
- Controlled crawling with queue-based exploration
# Phase 3 - Storage System

Goals: Persist data so the crawler can **restart safely**.
#### Database
- [ ] Setup database
- [ ] Create `pages` table
- [ ] Create `links` table
- [ ] Create `frontier` table
- [ ] Create `domains` table
#### Persistence
- [ ] Store crawled pages
- [ ] Store extracted links
- [ ] Persist frontier queue
- [ ] Support crawler restart

Deliverable:
- Crawler that can stop and resume safely
# Phase 4 - Robust Crawling

Goals: Make crawler **stable and respectful**.
- [ ] Add request timeout
- [ ] Add retry system
- [ ] Filter non-HTML content
- [ ] Implement `robots.txt` parsing
- [ ] Add domain rate limiting
- [ ] Detect duplicate content (hashing)

Deliverable:
- Reliable crawler that can run continuously
# Phase 5 - Curiosity Engine

Goals: Make the crawler **choose interesting pages**.
#### Curiosity Signals
- [ ] Implement novelty scoring
- [ ] Implement rarity scoring
- [ ] Implement domain novelty
- [ ] Implement exploration depth bonus
#### Curiosity Score
- [ ] Combine signals into final score
- [ ] Use score to prioritize URLs
- [ ] Track curiosity score history

Deliverable:
- Agent chooses pages based on curiosity

# Phase 6 - Research Mode

Goals: Enable **topic-driven exploration**.
#### Topic Processing
- [ ] Accept topic input
- [ ] Extract keywords from topic
- [ ] Compute topic relevance score
#### Topic Exploration
- [ ] Prioritize relevant pages
- [ ] Track topic clusters
- [ ] Build topic graph
#### Knowledge Graph
- [ ] Extract key concepts from pages
- [ ] Create topic nodes
- [ ] Create relationship edges
- [ ] Store knowledge graph
- [ ] Export graph structure

Deliverable:
- Agents build knowledge map for a topic.

# Phase 7 - Discovery Mode

Goals: Autonomous exploration of unusual content.
#### Weirdness Detection
- [ ] Detect rare vocabulary
- [ ] Detect deep URLs
- [ ] Detect old website structure
- [ ] Detect unusual domains
#### Discovery System
- [ ] Rank interesting pages
- [ ] Store discoveries
- [ ] Generate discovery feed
#### Daily Report
- [ ] Generate curiosity report
- [ ] List top discoveries
- [ ] Save discovery history

Deliverable:
- System discovers interesting websites.

# Phase 8 - Multi-Agent Exploration

Goals: Autonomous swarm exploration.
#### Agent Types
- [ ] Implement Scout Agent
- [ ] Implement Research Agent
- [ ] Implement Deep Diver Agent
#### Coordination
- [ ] Shared frontier
- [ ] Shared discovery database
- [ ] Agent scheduling

Deliverable:
- Multiple agent exploring simultaneously.

# Phase 9 - Visualization

Goals: Make exploration visible.
#### Exploration Graph
- [ ] Visualize visited pages
- [ ] Visualize link network
- [ ] Show exploration path
#### Knowledge Map
- [ ] Visualize topic clusters
- [ ] Visualize concept relationships
#### Discovery Dashboard
- [ ] Display interesting discoveries
- [ ] Display exploration statistics

Deliverable:
- Visual interface for exploration.

# Phase 10 - Advanced Intelligence
#### Learning Curiosity
- [ ] Track successful discoveries
- [ ] Adapt exploration strategies
- [ ] Implement curiosity learning
#### Strategy Evolution
- [ ] Compare agent performance
- [ ] Evolve exploration strategies

Deliverable:
- Self-improving exploration system
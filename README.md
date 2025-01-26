# DeepSeek Browser Automation Framework

## Agent Architecture

``` 
  [Task String] 
       │
       ▼
┌───────────────┐
│  Task Parser  │──▶ [Step 1: Navigate]
└───────────────┘    [Step 2: DOM Query]
       │             [Step 3: Input Fill]
       ▼             [Step N: Action Commit]
┌───────────────┐
│ Action Queue  │
└───────────────┘
       │
       ▼
┌───────────────────┐
│  LLM Processor    │
│ ┌───────────────┐ │
│ │ Vision Engine │←───[Page Screenshot]
│ └───────────────┘ │
└───────────────────┘
       │
       ▼
┌───────────────────┐
│ Browser Instance  │
│ ┌───────────────┐ │
│ │   WebDriver   │─┐│
│ └───────────────┘ ││
│ ┌───────────────┐ │
│ │   DevTools    │←┘
│ └───────────────┘ │
└───────────────────┘
```

## Implementation Examples

### Proton Mail Agent (`deepseek_proton_mail.py`)
```python
Agent(
    task="1. Navigate to proton.me\n2. Authenticate\n3. Compose email",
    llm=ChatOpenAI(model='deepseek-chat'),
    browser=Browser(
        headless=False,
        security_profile="enterprise"
    ),
    action_delay=1.2  # Human-like intervals
)
```
``` 
[Agent]                   [Browser]
   │                         │
   │──GET proton.me─────────▶│
   │◀─DOM+Metrics─────────────│
   │──Fill #username─────────▶│
   │──Fill #password─────────▶│
   │──Click .signin-btn──────▶│
   │◀─Nav Success─────────────│
```

### Reddit Automation (`deepseek_reddit.py`)
``` 
[Agent]                   [Reddit]
   │                         │
   │──OAuth2 Token──────────▶│
   │◀─Session Cookie─────────│
   │──POST /submit───────────▶│
   │◀─Post ID─────────────── ─│
   │──PUT /vote──────────────▶│
   │◀─200 OK──────────────────│
```

### YouTube Automation (`deepseek_youtube.py`)
``` 
[Agent]                   [YouTube]
   │                         │
   │──GET /──────────────────▶│
   │◀─Page DOM─────────────── │
   │──Fill search box────────▶│
   │──Click search button────▶│
   │◀─Results DOM─────────────│
   │──Click video result─────▶│
   │◀─Video Started───────────│
```

## Core Interaction Pattern
```
┌────────────┐   Chromium   ┌───────────┐
│  DeepSeek  │◀──Driver───▶ │  Browser  │
│   Agent    │  DevTools    │  Instance │
└──────┬─────┘ Protocol     └─────┬─────┘
       │                          │       
       └──────Page Interaction────┘
            • DOM Manipulation
            • Network Intercept
            • Performance Metrics
```

- Video discovery workflow
- Filter system integration
- Playback verification
- Adaptive wait conditions


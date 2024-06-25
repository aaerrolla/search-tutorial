# Elasticsearch Search Tutorial

This directory contains a starter Flask project used in the Search tutorial.

01- Added multi_match DSL in app.py

02 - Implementing pagination :  
        Using  size and from_ parameter    
        NOTE: since from is the keyword in python  from_ is used in elasticsearch python API  
        By default elastic returns first 10 records , if want to other than 10
        we need to pass size parameter in DSL
    Example 

```
results = es.search(
    query={
        'multi_match': {
            'query': query,
            'fields': ['name', 'summary', 'content'],
        }
    }, size=5
)
```

To access additional pages of results, the from_ parameter is used, which indicates 
from where in the complete list of results to start

```
results = es.search(
    query={
        'multi_match': {
            'query': query,
            'fields': ['name', 'summary', 'content'],
        }
    }, size=5, from_=5
)
```


    
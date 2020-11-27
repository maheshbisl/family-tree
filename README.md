# family-tree

## Problem
1. https://www.geektrust.in/coding-problem/backend/family

## Assumption / Limitations
1. No Duplicate names
2. Names cannot have spaces
3. Monogamous relationship
4. No Samesex Marriages

## Commands
* ADD_CHILD Mother Child Gender 
* ADD_SPOUSE Name Spouse
* GET_RELATIONSHIP Name Relationship

### Relationship:
- Mother
- Father
- Spouse
- Daughters
- Siblings
- Sons
- Brothers
- Sisters
- Paternal-Uncles
- Paternal-Aunts
- Maternal-Uncles
- Maternal-Aunts
- Uncles
- Aunts
- Sisters-In-Law
- Brothers-In-Law
- Siblings-In-Law

## CI/CD
1. GitHub actions
2. Check .github/workflows/test.yml

## Solution

### Data Structure
1. Dictionary of members with 'Name' as the key.
2. Each member of is a dictionary with properties { Spouse: String, Male: Boolean, Mother: String, Children: Array }

### Programming language
- Python 3.7

### Tested on
```Ubuntu 16.04 LTS (Xenial Xerus)```

## Testing
- Check `test.sh`

### Unit testing
- Run ``` python test.py```

### Run the application
- Run ```python family_tree.py test-input```

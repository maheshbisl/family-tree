# family-tree

## Problem
1. Build a family tree
2. Monogamous relationship
3. Traverse based on relationships
4. Add new members to the family

## Assumption / Limitations
1. No Duplicate names
2. Names cannot have spaces

## Commands
* ADD_CHILD Mother Child Gender 
* ADD_SPOUSE Name Spouse
* GET_RELATIONSHIP Name Relationship

### Relationship:
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
- Sisters-In-Law
- Brothers-In-Law

## CI/CD
1. GitHub actions
2. Check .github/workflows/test.yml

## Solution

### Data Structure
1. Dictionary of members with 'Name' as the key.
2. Each member of is a dictionary with properties { Spouse: String, Male: Boolean, Mother: String, Children: Array }

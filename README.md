# family-tree

## Problem
1. Build a family tree
2. Monogamous relationship
3. Traverse based on relationships
4. Add new members to the family

## Commands
* ADD_CHILD <Child's Mother>  <Child's name> <Gender> 
* GET_RELATIONSHIP <Member's name> <Relationship Name>

## Solution

### Data Structure
1. Dictionary of members with 'Name' as the key.
2. Each member of is a dictionary with properties { Spouse: String, Male: Boolean, Mother: String, Children: Array }


# Detailed Answer for Question 27 – Data Wrangling Operations in Pandas

## 1. Merge

Merge combines datasets using a common column.

### Example

```python
import pandas as pd

df1 = pd.DataFrame({
    "ID":[1,2],
    "Name":["Ram","Sam"]
})

df2 = pd.DataFrame({
    "ID":[1,2],
    "Marks":[80,90]
})

result = pd.merge(df1, df2, on="ID")

print(result)
```

### Output

| ID | Name | Marks |
|----|------|-------|
| 1 | Ram | 80 |
| 2 | Sam | 90 |

### Purpose
- Combines datasets using common columns.
- Similar to SQL joins.

---

## 2. Join

Join combines datasets using indexes.

### Example

```python
df1 = pd.DataFrame({
    "Name":["Ram","Sam"]
}, index=[1,2])

df2 = pd.DataFrame({
    "Marks":[80,90]
}, index=[1,2])

result = df1.join(df2)

print(result)
```

### Output

| index | Name | Marks |
|------|------|------|
| 1 | Ram | 80 |
| 2 | Sam | 90 |

### Purpose
- Joins DataFrames using index values.

---

## 3. Concatenation

Concatenation stacks datasets vertically or horizontally.

### Vertical Concatenation

```python
pd.concat([df1, df1], axis=0)
```

### Horizontal Concatenation

```python
pd.concat([df1, df2], axis=1)
```

### Purpose
- Combines multiple DataFrames.

---

## 4. Reindex

Reindex rearranges or creates new indexes.

### Example

```python
df = pd.DataFrame({
    "Marks":[80,90]
}, index=["A","B"])

print(df.reindex(["B","A","C"]))
```

### Output

| index | Marks |
|------|------|
| B | 90 |
| A | 80 |
| C | NaN |

### Purpose
- Rearranges rows.
- Adds missing labels.

---

## 5. set_index()

Converts a column into index.

### Example

```python
df = pd.DataFrame({
    "Name":["Ram","Sam"],
    "Marks":[80,90]
})

df2 = df.set_index("Name")

print(df2)
```

### Output

| Name | Marks |
|------|------|
| Ram | 80 |
| Sam | 90 |

### Purpose
- Makes column labels act as row indexes.

---

## 6. reset_index()

Restores default numeric indexes.

### Example

```python
df3 = df2.reset_index()

print(df3)
```

### Output

| index | Name | Marks |
|------|------|------|
| 0 | Ram | 80 |
| 1 | Sam | 90 |

### Purpose
- Converts index back into normal column.

---

# Difference Between Operations

| Function | Purpose |
|----------|----------|
| merge() | combine using common column |
| join() | combine using index |
| concat() | stack DataFrames |
| reindex() | rearrange/add indexes |
| set_index() | convert column into index |
| reset_index() | restore default index |

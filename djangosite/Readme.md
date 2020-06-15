## 當報價單上有多個line (即有多個設備時，要另外產生equipment 的資料) 

```log
document.Document.equipment: (fields.E304) Reverse accessor for 'Document.equipment' clashes with reverse accessor for 'Inspection.equipment'.
        HINT: Add or change a related_name argument to the definition for 'Document.equipment' or 'Inspection.equipment'.
document.Document.equipment: (fields.E305) Reverse query name for 'Document.equipment' clashes with reverse query name for 'Inspection.equipment'.
        HINT: Add or change a related_name argument to the definition for 'Document.equipment' or 'Inspection.equipment'.
inspection.Inspection.equipment: (fields.E304) Reverse accessor for 'Inspection.equipment' clashes with reverse accessor for 'Document.equipment'.
        HINT: Add or change a related_name argument to the definition for 'Inspection.equipment' or 'Document.equipment'.
inspection.Inspection.equipment: (fields.E305) Reverse query name for 'Inspection.equipment' clashes with reverse query name for 'Document.equipment'.
        HINT: Add or change a related_name argument to the definition for 'Inspection.equipment' or 'Document.equipment'.
```
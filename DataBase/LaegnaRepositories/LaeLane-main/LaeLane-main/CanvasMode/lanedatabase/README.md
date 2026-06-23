# Lane Database — Essential Combinatorics (R/T Model)

## Purpose
This directory contains the minimal, clean, and learnable structure of the Lane system.  
It defines the **R/T combinatorics** that underlie all lane geometries, projections, and projective interpretations.  
Graphics and rendering aspects will be added later; this document focuses only on the essential structure.

## Structure
```
simpRs/
  R0.5/
    (comment: expected T-folders)
  R1/
    (comment: expected T-folders)
  R2/
    (comment: expected T-folders)
  R3/
    (comment: expected T-folders)
  R4/
    (comment: expected T-folders)
```

- **R-folders exist** and represent digit-length partitions.  
- **T-folders may not exist yet**, but each R-folder contains a comment pointing to the correct T-folder.  
- This makes the structure **AI-readable**, **predictable**, and **self-describing** even before full data is added.

## Why R/T Exists
The R/T model expresses a fundamental inversion:

- **R** partitions the *exponential* growth of the number space.  
- **T** enumerates the *linear* sequence within each exponential block.  

This alternation between **linear** and **exponential** is not arbitrary; it is a natural extension of Laegna logic.  
Each level of abstraction in Laegna mathematics alternates between these two modes.

## What a Lane Is
A Lane is an **ideal ordered line**:

- **Linear** in its own coordinate system  
- **Exponential** in its underlying number structure  
- **Projective** because it compresses exponential hierarchy into a linear geometric form  
- **Projected** because it maps internal number structure into geometry  

This duality explains why lanes feel simultaneously simple and deeply structured.

## Why Comments Point to Missing T-Folders
Each R-folder contains a forward-declaration comment:

- Declares the intended T-folder  
- Allows AI to reconstruct the full tree  
- Enables workload planning (small samples, progressive deepening, or full dataset)  
- Prevents misinterpretation of empty folders  
- Keeps the combinatorics clean and predictable  

This is the best form for early development.

## Current Understanding
The lane system is now fully intelligible at the combinatorial level:

- Projection meaning is clear  
- Projective meaning is clear  
- Linear/exponential alternation is explicit  
- R/T inversion is natural, not exceptional  
- Higher levels can already be built mathematically  

This README documents the essential part of that understanding.

## Future Section: Graphics
A later section will describe:

- projection modes  
- geometric interpretation  
- rendering strategies  
- fractalization  
- 2D/3D modes  

This is intentionally omitted here to keep the core combinatorics clean.

---
marp: true
paginate: true
theme: custom
---

# Handbook: `custom` theme





---

## Configurations
1. Declare directive `theme: custom`
2. Enable HTML in Marp configs
3. Add path to `custom.css` theme in Marp configs






---

## Le texte

### Accent Bold

```html
<b class="important"></b>
```
### Accent Italic

```html
<i class="important"></i>
```




---

## Les blocks

### Standard

```md
<div class="block">
    
<i class="block-icon fas fa-cloud"></i> 

## Title

Content ...

</div>
```

<div class="block">
    
<i class="block-icon fas fa-cloud"></i> 

## Title

Content ...

</div>




---

### Info 
```md
<div class="block note">
    
<i class="block-icon fas fa-info"></i> 

...

</div>
```
<div class="block note">
    
<i class="block-icon fas fa-info"></i> 

...

</div>




---

### Warning 
```md
<div class="block warning">
    
<i class="block-icon fas fa-exclamation"></i> 

# A retenir

La terre est ronde

</div>
```

<div class="block warning">
    
<i class="block-icon fas fa-exclamation"></i> 

# A retenir

La terre est ronde

</div>



---

## Les layouts

### Horizontal separation (2 sides)

```md
<div class="flex-horizontal">
<div class="flex">

Left section

</div>
<div class="flex">

Right section

</div>
</div>
```

<div class="flex-horizontal">
<div class="flex">

Left section

</div>
<div class="flex">

Right section

</div>
</div>



---

### Horizontal separation (3 sides)

```md
<div class="flex-horizontal">
<div class="flex">

Left section

</div>
<div class="flex">

Center section

</div>
<div class="flex">

Right section

</div>
</div>
```

<div class="flex-horizontal">
<div class="flex">

Left section

</div>
<div class="flex">

Center section

</div>
<div class="flex">

Right section

</div>
</div>

---

### Horizontal separation (inequal)

```md
<div class="flex-horizontal">
<div class="flex" style="flex:0.3">

Left section

</div>
<div class="flex" style="flex:0.7">

Right section

</div>
</div>
```

<div class="flex-horizontal">
<div class="flex" style="flex:0.3">

Left section

</div>
<div class="flex" style="flex:0.7">

Right section

</div>
</div>

---
## Les pages spéciales

### Cover

```md
<div class="coverBlockCenter">

<div class="coverModuleName">Nom du module</div>
<div class="coverCourseName"><span class="important">#1 </span>Nom du cours</div>
<div class="coverAuthor">par <span class="important">Prénom Nom</span></div>

</div>

<img class="coverFooterLeft" height="60px" src="assets/logo.png" />
<div class="coverYear coverFooterRight">Date ou Année</div>
```

### Partie
```md
<div class="main">

# 01 

## Nom de la partie

</div>
```

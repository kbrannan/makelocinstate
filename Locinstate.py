import arcpy
# input info
chr_dir_work = r'\\Deqhq1\tmdl\TMDL_WR\MidCoast\GIS\Figures\python\makelocinstate'
chr_map_doc_base = r'\\Deqhq1\tmdl\TMDL_WR\MidCoast\GIS\BacteriaTMDL\General\MapDocs\Midcoast-Basin-Location-in-StateDraft00201709271518.mxd'
chr_map_doc_new = chr_dir_work + r'\loc_example.mxd'
chr_png_map_new = chr_dir_work + r'\loc_example.png'
chr_lyr_name_sel = r'HUC 08'
chr_lyr_sym_wtsd = r'\\Deqhq1\tmdl\TMDL_WR\MidCoast\GIS\Layer\locate_in_state_watershed_boundary.lyr'
chr_lyr_sym_state = r'\\Deqhq1\tmdl\TMDL_WR\MidCoast\GIS\Layer\locate_in_state_OR_boundary.lyr'
# get the base map document
mxd_base = arcpy.mapping.MapDocument(chr_map_doc_base)
# make a copy that will be changed
mxd_base.saveACopy(chr_map_doc_new)
del mxd_base
# get new map doc to edit
mxd_new = arcpy.mapping.MapDocument(chr_map_doc_new)
# get layers in the document and print out the data sources and the layer names
layers = arcpy.mapping.ListLayers(mxd_new)
print '\n' + r'Data sources of layers'
for layer in layers:
    if layer.supports("dataSource"): # some layers might not support the property "dataSource"
        print layer.dataSource
print '\n' + r'Names of layers'
for layer in layers:
    desc = arcpy.Describe(layer)
    print desc.nameString
# get the data frame of the map doc
df = arcpy.mapping.ListDataFrames(mxd_new)[0]
# get the watershed layer in map doc
lyr_wtsd = arcpy.mapping.ListLayers(mxd_new, chr_lyr_name_sel, df)[0]
# get the watershed boundary and state layers that have the symbology to be used
lyr_sym_wtsd = arcpy.mapping.Layer(chr_lyr_sym_wtsd)
lyr_sym_state = arcpy.mapping.Layer(chr_lyr_sym_state)
# change the symbology of the watershed boundary in map doc to that of the symbology of the layer file
arcpy.mapping.UpdateLayer(df,lyr_wtsd, lyr_sym_wtsd)
# reset the map extent to that of the state layer file
df.extent = lyr_sym_state.getExtent()
# save map doc
mxd_new.save()
# export map to PNG file
arcpy.mapping.ExportToPNG(mxd_new,chr_png_map_new, resolution=300)

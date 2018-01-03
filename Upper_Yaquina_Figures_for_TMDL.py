import arcpy

#input info in same way as Mid-Coast map outline
#created new .lyr and .mxd files specific to upper yaquina watershed

chr_dir_work = r'\\DEQHQ1\TMDL_WR\MidCoast\GIS\Figures\python\makelocinstate'
chr_map_doc_base = r'\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\Upper_Yaquina_TMDL_BC_Automated_V2.mxd'
chr_map_doc_new = r'\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\python\makelocinstate\Upper_Yaquina_KMB.mxd'
chr_png_map_new = r'\\DEQHQ1\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\Up_Yaq.png'
chr_lyr_name_sel = r'HUC 10'
chr_lyr_sym_wtsd = r'\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Layer\upper_yaquina_official_huc_10.lyr'
chr_lyr_sym_state = r'\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\or_state_boundary_for_inset.lyr'

# get the base map document

mxd_base = arcpy.mapping.MapDocument(chr_map_doc_base)
# make a copy that will be changed

mxd_base.saveACopy(chr_map_doc_new)
del mxd_base
# get new map doc to edit
mxd_new = arcpy.mapping.MapDocument(chr_map_doc_new)
layers = arcpy.mapping.ListLayers(mxd_new)
print '\n' + r'Data sources of layers'
for layer in layers:
    if layer.supports("dataSource"):
        print layer.dataSource
# some layers might not support the property "dataSource"
print '\n' + r'Names of layers'
#getting an error on line 32: what is the purpose of using the Describe function here?
# use the following command to get the layer file and create a layer object in your code
layerCur = arcpy.mapping.Layer(r'\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\or_state_boundary_for_inset.lyr')
# then you can get it's properties and maniputale it
print layerCur.name
# the describe command only works on objects that are created within arcpy, but you don't have to use it with the layer object
#desc = arcpy.Describe(r'\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\or_state_boundary_for_inset.lyr')
#print desc.nameString
#print desc

for layer in layers:
    desc = arcpy.Describe(r'\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\or_state_boundary_for_inset.lyr')
    print desc.nameString

# get the data frame of the map doc
df = arcpy.mapping.ListDataFrames(mxd_new)[0]
# get the watershed layer in map doc
lyr_wtsd = arcpy.mapping.ListLayers(mxd_new, chr_lyr_name_sel, df)[0]
# get the watershed boundary and state layers that have the symbology to be used
    #lyr_sym_wtsd = arcpy.mapping.Layer(chr_lyr_sym_wtsd)
    #lyr_sym_state = arcpy.mapping.Layer(chr_lyr_sym_state)
# change the symbology of the watershed boundary in map doc to that of the symbology of the layer file
    #arcpy.mapping.UpdateLayer(df,lyr_wtsd, lyr_sym_wtsd)
# reset the map extent to that of the state layer file
    #df.extent = lyr_sym_state.getExtent()
# save map doc
    #mxd_new.save()
# export map to PNG file
    #arcpy.mapping.ExportToPNG(mxd_new,chr_png_map_new, resolution=300)






#mxd_base = arcpy.mapping.MapDocument(r'\\U:\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\Upper_Yaquina_TMDL_BC_Automated_V2.mxd')


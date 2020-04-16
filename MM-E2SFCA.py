#-------------------------------------------------------------------------------
# Name:        MM-E2SFCA
# Purpose:     Multimodal enhanced two-step floating catchment area model
#              using street networks and impedance coefficients included in the
#              following dataset: https://doi.org/
# Note:        Dataset is implemented using the proprietary ArcPy module.
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
# Import arcpy module
import arcpy, os

#Parameters, range(start, stop, step)
##ps = range(140,321,30)
##qs = range(440,1041,100)
ps = range(290,321,30)
qs = range(440,1041,100)
#ps = range(140,160,15)
#qs = range(440,500,50)
arcpy.env.overwriteOutput = True
resultfolder = os.getcwd()
for p in ps:
    for q in qs:
        arcpy.AddMessage("Running p = {0}, q = {1}.".format(p,q))
        # Local variables:
        ODmatrix_Car = "ODmatrix_Car"
        ODmatrix_Car__7_ = "ODmatrix_Car"
        ODmatrix_bus2 = "ODmatrix_bus2"
        ODmatrix_Car__6_ = "ODmatrix_Car"
        ODmatrix_Car__13_ = "ODmatrix_Car"
        ODmatrix_bus2__6_ = "ODmatrix_bus2"
        ODmatrix_Car__2_ = "ODmatrix_Car"
        ODmatrix_Car__17_ = "ODmatrix_Car"
        ODmatrix_Car__23_ = ODmatrix_Car__17_
        ODmatrix_Car__21_ = ODmatrix_Car__23_
        PCPlocation_metro__6_ = "PCPlocation_metro"
        PCPlocation_metro__7_ = PCPlocation_metro__6_
        ODmatrix_Car__18_ = "ODmatrix_Car"
        ODmatrix_Car__22_ = ODmatrix_Car__18_
        ODmatrix_Car__16_ = ODmatrix_Car__22_
        ODmatrix_Car__5_ = ODmatrix_Car__16_
        ODmatrix_Car__4_ = ODmatrix_Car__5_
        # change
        gaussian_car = resultfolder+"\\gaussian_car"+'_p_'+str(p)+'_q_'+str(q)
        PCPlocation_metro__3_ = PCPlocation_metro__7_
        ODmatrix_bus__3_ = "ODmatrix_bus2"
        ODmatrix_bus__12_ = ODmatrix_bus__3_
        ODmatrix_bus__9_ = ODmatrix_bus__12_
        ODmatrix_Car__9_ = ODmatrix_bus__9_
        ODmatrix_bus2__12_ = ODmatrix_Car__9_
        #change
        gaussian_bus = resultfolder+"\\gaussian_bus"+'_p_'+str(p)+'_q_'+str(q)
        #change
        GaussianPCP = resultfolder+"\\bus\\GaussianPCP"+'_p_'+str(p)+'_q_'+str(q)
        GaussianPCP__3_ = GaussianPCP
        GaussianPCP__8_ = GaussianPCP__3_
        ODmatrix_bus__13_ = "ODmatrix_bus2"
        ODmatrix_Car__3_ = ODmatrix_Car__21_
        #change
        AK_CarGaussian = resultfolder+"\\AK_CarGaussian"+'_p_'+str(p)+'_q_'+str(q)
        ODmatrix_bus__10_ = "ODmatrix_bus2"
        ODmatrix_bus__14_ = ODmatrix_bus__10_
        ODmatrix_bus__6_ = ODmatrix_bus__13_
        #change
        AK_BusGaussian = resultfolder+"\\AK_BusGaussian"+'_p_'+str(p)+'_q_'+str(q)
        ODmatrix_bus2__9_ = "ODmatrix_bus2"
        ODmatrix_Car__11_ = "ODmatrix_Car"
        ODmatrix_Car__14_ = "ODmatrix_Car"
        ODmatrix_bus2__11_ = "ODmatrix_bus2"
        ODmatrix_bus2__14_ = "ODmatrix_bus2"
        ODmatrix_bus2__4_ = "ODmatrix_bus2"
        ODmatrix_bus2__17_ = "ODmatrix_bus2"
        ODmatrix_bus = "ODmatrix_bus2"
        ODmatrix_bus__4_ = "ODmatrix_bus2"
        ODmatrix_Car__8_ = "ODmatrix_Car"
        GaussianPCP__7_ = "GaussianPCP"
        ODmatrix_bus__8_ = "ODmatrix_bus2"
        GaussianPCP__2_ = "GaussianPCP"
        ODmatrix_Car__12_ = "ODmatrix_Car"
        ODmatrix_bus__7_ = "ODmatrix_bus2"
        ODmatrix_Car__15_ = "ODmatrix_Car"
        ODmatrix_bus__5_ = "ODmatrix_bus2"
        GaussianPCP__9_ = "GaussianPCP"
        ODmatrix_Car__19_ = "ODmatrix_Car"
        ODmatrix_bus__2_ = "ODmatrix_bus2"
        GaussianPCP__11_ = "GaussianPCP"

        # Process: Add Field (6)
        arcpy.AddField_management(ODmatrix_Car__17_, "AkCar2", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: Add Field
        arcpy.AddField_management(ODmatrix_Car__18_, "linearW", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: Calculate Field
        ##230
        arcpy.CalculateField_management(ODmatrix_Car__22_, "linearW", "val", "VB", "Dim val\\n\\nIf [Total_Trav] < 10  Then\\nval = Exp (-5* 5/"+str(p)+")\\nelseif [Total_Trav] > 20 Then\\nval = Exp (-25* 25/"+str(p)+" )\\nelse\\n     val = Exp (-15* 15/"+str(p)+")\\nend if\\n")
        arcpy.AddField_management(ODmatrix_Car__16_, "PkWk", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: Calculate Field (2)
        arcpy.CalculateField_management(ODmatrix_Car__5_, "PkWk", "[POPWCar] * [linearW]", "VB", "")

        # Process: Summary Statistics
        arcpy.Statistics_analysis(ODmatrix_Car__4_, gaussian_car, "PkWk SUM", "PCPID")

        # Process: Add Join
        arcpy.AddJoin_management(PCPlocation_metro__6_, "PCPID", gaussian_car, "PCPID", "KEEP_COMMON")

        # Process: Add Field (3)
        arcpy.AddField_management(ODmatrix_bus__3_, "linearW", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: Calculate Field (3)
        ##740
        arcpy.CalculateField_management(ODmatrix_bus__12_, "linearW", "val", "VB", "Dim val\\n\\nIf [Ave_Total_] < 10  Then\\nval = Exp (-5* 5/"+str(q)+" )\\nelseif ([Ave_Total_] >= 10 And  [Ave_Total_]) < 20 Then\\nval = Exp (-15* 15/"+str(q)+" )\\nelseif [Ave_Total_] > 30 Then\\nval = Exp (-45* 45/"+str(q)+" )\\nelse\\n     val = Exp (-25* 25/"+str(q)+" )\\nend if\\n")

        # Process: Add Field (4)
        arcpy.AddField_management(ODmatrix_bus__9_, "PkWk", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: Calculate Field (4)
        arcpy.CalculateField_management(ODmatrix_Car__9_, "PkWk", "[linearW] * [POPWoCar]", "VB", "")

        # Process: Summary Statistics (2)
        arcpy.Statistics_analysis(ODmatrix_bus2, gaussian_bus, "PkWk SUM", "PCPID")

        # Process: Add Join (2)
        arcpy.AddJoin_management(PCPlocation_metro__7_, "PCPlocation_metro.PCPID", gaussian_bus, "PCPID", "KEEP_ALL")

        # Process: Copy Features
        arcpy.CopyFeatures_management(PCPlocation_metro__3_, GaussianPCP, "", "0", "0", "0")

        # Process: Add Field (5)
        arcpy.AddField_management(GaussianPCP, "RJ", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: Calculate Field (5)
        #change
        gcPre = "gaussian_car"+'_p_'+str(p)+'_q_'+str(q)
        gbPre = "gaussian_bus"+'_p_'+str(p)+'_q_'+str(q)
        gpPre = "GaussianPCP"+'_p_'+str(p)+'_q_'+str(q)
        arcpy.CalculateField_management(GaussianPCP__3_, "RJ", "val", "VB", "Dim val\\n\\nIf IsNull (["+gbPre+"_SUM_PkWk])  Then\\nval = [PCPlocation_metro_Cnt_latlon] / ["+gcPre+"_SUM_PkWk] \\n\\nelse\\n     val = [PCPlocation_metro_Cnt_latlon] / (["+gcPre+"_SUM_PkWk] + ["+gbPre+"_SUM_PkWk] )\\n\\nend if")

        # Process: Add Join (3)
        arcpy.AddJoin_management(ODmatrix_Car__23_, "PCPID", GaussianPCP__8_, "PCPlocation_metro_PCPID", "KEEP_ALL")

        # Process: Calculate Field (6)
        arcpy.CalculateField_management(ODmatrix_Car__21_, "ODmatrix_Car.AkCar2", "["+gpPre+".RJ] * [ODmatrix_Car.linearW]", "VB", "")

        # Process: Summary Statistics (3)
        arcpy.Statistics_analysis(ODmatrix_Car__3_, AK_CarGaussian, "ODmatrix_Car.AkCar2 SUM", "ODmatrix_Car.BlockGroup")

        # Process: Add Field (7)
        arcpy.AddField_management(ODmatrix_bus__10_, "AkBus2", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

        # Process: Add Join (4)
        arcpy.AddJoin_management(ODmatrix_bus__14_, "PCPID", GaussianPCP__8_, "PCPlocation_metro_PCPID", "KEEP_ALL")

        # Process: Calculate Field (7)
        arcpy.CalculateField_management(ODmatrix_bus__13_, "ODmatrix_bus2.AkBus2", "["+gpPre+".RJ] * [ODmatrix_bus2.linearW]", "VB", "")

        # Process: Summary Statistics (4)
        arcpy.Statistics_analysis(ODmatrix_bus__6_, AK_BusGaussian, "ODmatrix_bus2.AkBus2 SUM", "ODmatrix_bus2.BGFIPS")

        ## reomove join
        arcpy.RemoveJoin_management(PCPlocation_metro__6_, "")
        arcpy.RemoveJoin_management(ODmatrix_Car__17_, "")
        arcpy.RemoveJoin_management(ODmatrix_bus__10_, "")
        #PCPlocation_metro__6_
        #ODmatrix_Car__17_
        #ODmatrix_bus__10_
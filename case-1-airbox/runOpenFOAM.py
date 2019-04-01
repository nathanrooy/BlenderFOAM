def main(foldername_new):
    import os
    #---RUN OpenFOAM--------------------------------------------+
    os.chdir(foldername_new + '/')
    print 'Running [surfaceFeatureExtract] ----------------------------------------'
    os.system('surfaceFeatureExtract -includedAngle 120 constant/triSurface/airBoxMesh_oriented.stl airBoxMesh') # surfaceFeatureExtract<<<<<<<<<<<<<<<<<<<<<<<<<<
    print 'Running [OpenFOAM] -----------------------------------------------------'
    os.system('chmod +x Allrun')
    os.system('./Allrun')   # [works only when called from the terminal...]

    print 'Collecting Results------------------------------------------------------'
    os.system('patchAverage p airBox_abInlet -latestTime >pInlet.txt')      # inlet pressure       

    #---RETURN BACK TO MAIN DIRECTORY
    os.chdir('../')

    return

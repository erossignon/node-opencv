{
  "targets": [{ 
      "target_name": "opencv"
      , "sources": [ 
          "src/init.cc"
        , "src/Matrix.cc"
        , "src/OpenCV.cc"
        , "src/CascadeClassifierWrap.cc"
        , "src/Contours.cc"
        , "src/Point.cc"
        , "src/VideoCaptureWrap.cc"
        , "src/CamShift.cc"
        ]
      , "conditions": [

        ['OS=="linux"',  {
        
            'libraries': [ '<!@(pkg-config --libs opencv)'  ],
            'cflags': ['<!@(pkg-config --cflags --libs opencv)', '-Wall'],
            'cflags!' : [ '-fno-exceptions'],
            'cflags_cc!': [ '-fno-rtti',  '-fno-exceptions'],
        
        }],

        ['OS=="mac"', {

            'libraries': [ '<!@(pkg-config --libs opencv)'  ],
            'cflags': ['<!@(pkg-config --cflags --libs opencv)', '-Wall'],
            'cflags!' : [ '-fno-exceptions'],
            'cflags_cc!': [ '-fno-rtti',  '-fno-exceptions'],

            # cflags on OS X are stupid and have to be defined like this
            'xcode_settings': {
              'OTHER_CFLAGS': [
                '<!@(pkg-config --cflags opencv)'
              ]
              , "GCC_ENABLE_CPP_RTTI": "YES"
              , "GCC_ENABLE_CPP_EXCEPTIONS": "YES"
            }
        }] ,

        ['OS=="win"', 
            {
              'include_dirs':['$(OPENCV_ROOT)/build/include', '$(OPENCV_ROOT)/build/include/opencv'],              
              'library_dirs':['$(OPENCV_ROOT)/build/x64/vc10/staticlib'],
              'libraries':[
                '-lopencv_core243.lib', 
                '-lopencv_imgproc243.lib', 
                '-lopencv_calib3d243.lib',
                '-lopencv_features2d243.lib', 
                '-lopencv_objdetect243.lib', 
                '-lopencv_video243.lib', 
                '-lopencv_highgui243.lib', 
                '-lopencv_contrib243.lib', 
                '-lopencv_flann243.lib', 
                '-lopencv_ml243.lib', 
                '-lopencv_gpu243.lib', 
                '-lopencv_legacy243.lib',
                '-lzlib.lib',
                '-llibjasper.lib',
                '-llibjpeg.lib',
                '-llibpng.lib',
                '-llibtiff.lib', 
                '-lcomctl32.lib',
                '-lvfw32.lib',
                '-lIlmImf.lib'
              ], 
        }]             
    ],

    "msvs_settings": {

      'VCLinkerTool': {         
        'AdditionalLibraryDirectories': [  '$(OPENCV_ROOT)/build/x64/vc10/staticlib'      ]       
      }    
    }   
  }]
}


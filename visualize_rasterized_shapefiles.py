import matplotlib.pyplot as plt
import gdal
import os


def main():
    all_districts = ["abbottabad", "battagram", "buner", "chitral", "hangu", "haripur", "karak", "kohat", "kohistan", "lower_dir", "malakand", "mansehra",
                     "nowshehra", "shangla", "swat", "tor_ghar", "upper_dir"]
    path = "E:\\Forest Cover - Redo 2020\\Google Cloud - Training\\Training Data\\District_Shapefiles_as_Clipping_bands\\"
    this_shapefile_path = os.path.join(path, f"{all_districts[16]}_shapefile.tif")
    ds = gdal.Open(this_shapefile_path)
    assert ds.RasterCount == 1
    shapefile_mask = ds.GetRasterBand(1).ReadAsArray()
    print(f"Shape: {shapefile_mask.shape}")
    plt.imshow(shapefile_mask)
    plt.show()
    pass


if __name__ == "__main__":
    main()

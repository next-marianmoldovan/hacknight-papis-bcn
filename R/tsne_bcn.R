library(Matrix)

# loading data into R

myfeatures <- read.table('/home/enrique/proyectos/papis/hacknight-papis-bcn/features_sorted_f.csv', sep=",", header=FALSE, stringsAsFactors=F)

for (i in 1:2048) {
  myfeatures[,i] <- as.numeric(myfeatures[,i])
}
mydata <- as.data.frame.matrix(myfeatures)

# load the Rtsne package
library(Rtsne)

rtsne_out <- Rtsne(as.matrix(mydata), dims=4, pca=TRUE, perplexity=10, check_duplicates=FALSE)
library(plotrix)
library(rgl)
library(plot3D)
open3d()
rgl.texts(rtsne_out$Y[,1], rtsne_out$Y[,2], rtsne_out$Y[,3], rownames(mydata), color = color.scale(rtsne_out$Y[,4], color.spec="hsv") )






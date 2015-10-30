import com.roy_scala.ml.d_cluster.d_cluster
import com.roy_scala.util.mil
import com.roy_scala.util.IO
import com.roy_scala.ml.d_cluster
import com.roy_scala.util.json

/**
 * Created by roy on 2015/10/26.
 */

object test {
  def main(args: Array[String]):Unit = {
    /*
    val my_list = List("a", "b", "c")
  val my_array = my_list.mkString("OK", "X", "bbb")
  println(my_array)
    val folder_path = "D:\\workspace\\SimplyBrand\\palas_svm\\corpos\\百科"
    val files = IO.FileIO.listFiles(folder_path)
    for (file <- files)
      println(file.getAbsolutePath)
    */

    val json_path = "C:\\Users\\roy\\Desktop\\test_scala_fileio.txt"
    /*
    val json_obj = json.parse_json_from_file(json_path) match {
      case List => json.parse_json_from_file(json_path)
      case other => println("JSON Related Error Occured")
    }
    */

    val json_obj = json.parse_json_from_file(json_path)
    println(json_obj.toString)

    //[{"token": "c:\\data\\1.txt", "content": "today is a good day"}, ... ]
    // val data = Array(Map("token" -> "aaa", "content" -> "bbb"), Map("token" -> "ccc", "content" -> "ddd"), Map("token" -> "cdcc", "content" -> "ddxxd"))
    val data = json_obj.asInstanceOf[Array[Map[String, String]]]

    val threshold:Float = 0.4f
    val kernel= (x:String, y:String) => 0.5f

    val d_cluster = new d_cluster(data, threshold, kernel)
    d_cluster.test_integrity()
    val clu = d_cluster.clustering()
    println(clu.deep.mkString(" "))

  }
}


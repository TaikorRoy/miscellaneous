package com.roy_scala.util

/**
 * Created by Roy on 22/10/2015.
 */

import java.io._
import scala.io.Source

object IO {
  object FileIO {
   def read(file_path: String): String = {
     val file = Source.fromFile(file_path)
     val content = file.mkString
     file.close()
     return content
      }

    def write(file_path: String, content: String): Unit = {
     val writer = new PrintWriter(new File(file_path))
      writer.write(content)
      writer.close()
    }
   }
}



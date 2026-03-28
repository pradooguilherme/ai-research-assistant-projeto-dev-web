package com.airesearch.backend.repository;

import com.airesearch.backend.model.Document;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.Collection;

@Repository
public interface DocumentRepository extends JpaRepository<Document, Long> {
    @Query(
            value =  "SELECT * FROM Document ORDER BY title LIMIT 100",
            nativeQuery = true
    )
    Collection<Document> findFirst100Documents();
}

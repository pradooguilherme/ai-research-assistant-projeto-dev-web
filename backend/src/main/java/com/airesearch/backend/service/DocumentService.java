package com.airesearch.backend.service;

import com.airesearch.backend.model.Document;

public interface DocumentService {
    Iterable<Document> findAll();
    Iterable<Document> findFirst100Documents();
    Document findById(Long id);
    void insert(Document document);
    void update(Long id, Document document);
    void delete(Long id);
}

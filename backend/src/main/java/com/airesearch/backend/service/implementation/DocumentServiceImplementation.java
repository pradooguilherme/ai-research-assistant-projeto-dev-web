package com.airesearch.backend.service.implementation;

import com.airesearch.backend.model.Document;
import com.airesearch.backend.repository.DocumentRepository;
import com.airesearch.backend.service.DocumentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class DocumentServiceImplementation implements DocumentService {

    private final DocumentRepository documentRepository;

    public DocumentServiceImplementation(DocumentRepository documentRepository){
        this.documentRepository = documentRepository;
    }

    @Override
    public Iterable<Document> findAll() {
        return documentRepository.findAll();
    }

    @Override
    public Document findById(Long id) {
        Optional<Document> document = documentRepository.findById(id);
        return document.orElse(null);
    }

    @Override
    public void insert(Document document) {
        documentRepository.save(document);
    }

    @Override
    public void update(Long id, Document document) {
        Optional<Document> documentOptional = documentRepository.findById(id);

        if(documentOptional.isPresent()) {
            documentRepository.save(document);
        }
    }

    @Override
    public void delete(Long id) {
        documentRepository.deleteById(id);
    }
}

import React, { useState, useEffect } from 'react';
import { GetTables } from '../../application/get-tables';
import { ApiTableRepository } from '../../infrastructure/api-table-repository';
import { Table } from '../../domain/entities';

function App() {
  const [tables, setTables] = useState<Table[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const getTables = new GetTables(new ApiTableRepository());
    getTables.execute()
      .then(setTables)
      .catch(err => setError(err.message));
  }, []);

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h1>Snowflake Table Catalog</h1>
      <table>
        <thead>
          <tr>
            <th>Catalog</th>
            <th>Schema</th>
            <th>Name</th>
            <th>Type</th>
            <th>Rows</th>
            <th>Bytes</th>
            <th>Created</th>
          </tr>
        </thead>
        <tbody>
          {tables.map(table => (
            <tr key={`${table.TABLE_CATALOG}-${table.TABLE_SCHEMA}-${table.TABLE_NAME}`}>
              <td>{table.TABLE_CATALOG}</td>
              <td>{table.TABLE_SCHEMA}</td>
              <td>{table.TABLE_NAME}</td>
              <td>{table.TABLE_TYPE}</td>
              <td>{table.ROW_COUNT}</td>
              <td>{table.BYTES}</td>
              <td>{table.CREATED}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;